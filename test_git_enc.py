#!/usr/bin/env python3

import unittest
from git_enc import find_kvs_at

class GitencTest(unittest.TestCase):
    def setUp(self):
        self.d = {
                    'lv1-1': {
                        'lv2-1': {
                            'k1': 'v1', 
                            'k2': 'v2'
                        }, 
                        'lv2-2': {
                            'k3': 'v3'
                        }
                    },
                    'lv1-2': {
                        'jin': 'choi'
                    }
                }

    def test_find_path_at(self):
        actual = list(find_kvs_at(self.d, 'lv1-1'))
        expected = [('k1','v1'), ('k2','v2'), ('k3','v3')]
        self.assertEqual(actual, expected)

unittest.main()
