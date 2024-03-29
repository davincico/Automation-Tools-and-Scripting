#!/usr/bin/env python
##
# check directory of files or single file against VirusTotal
# requires public VT API key
#
# - will provide pretty-ish JSON results (minus 'scan' field for found hashes)
# - optionally ignore non-discovered files
#
# author: adam m. swanda
# https://github.com/deadbits/malware-analysis-scripts
##

import json
import requests
import argparse
import hashlib
import os
import sys


def get_report(md5, f):
    params = {'resource': md5, 'apikey': api_key}
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    try:
        req = requests.get(url, params=params)
        json_data = req.json()
        if json_data['response_code'] == 1:
            del json_data['scans']
            return json_data
    except:
        pass
    return None


def display_report(md5, file_name):
    res = get_report(md5, file_name)
    if res is not None:
        print '\n'
        print '[ %s ]' % file_name
        print json.dumps(res, indent=4)
    else:
        if not ignore:
            print 'not found: %s (%s)' % (file_name, md5)


def get_md5(file_name):
    fin = open(file_name, 'rb')
    m = hashlib.md5()
    while True:
        data = fin.read(16384)
        if not data:
            break
        m.update(data)
    return m.hexdigest()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='simple check to determine if the files in a directory exist in VirusTotal')
    parser.add_argument('-a', '--apikey', help='virustotal public api key',
        action='store', required=True)
    parser.add_argument('-d', '--directory', help='absolute path to directory of samples',
        action='store', required=False)
    parser.add_argument('-f', '--file', help='absolute path to single sample',
        action='store', required=False)
    parser.add_argument('-i', '--ignore', help='ignore files that are not found',
        action='store_true', required=False,
        default=True)
    args = parser.parse_args()

    api_key = args.apikey
    ignore = args.ignore

    if not args.file and not args.directory:
        print 'error: must specify --file or --directory'
        sys.exit(1)

    if args.directory and not os.path.exists(args.directory):
        print 'error: directory %s not found' % args.directory
        sys.exit(1)

    if args.file and not os.path.exists(args.file):
        print 'error: file %s not found' % args.file
        sys.exit(1)


    if args.directory:
        hash_queue = {}
        print 'reading contents of %s' % args.directory
        all_files = os.listdir(args.directory)
        for f in all_files:
            if not os.path.isdir(args.directory + '/' + f):
                display_report(get_md5(args.directory + '/' + f), f)
            else:
                pass

    elif args.file:
        display_report(get_md5(args.file), args.file)