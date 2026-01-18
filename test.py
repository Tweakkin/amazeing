# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mramidam <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/18 18:02:23 by mramidam          #+#    #+#              #
#    Updated: 2026/01/18 18:02:38 by mramidam         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python

from typing import Dict
import argparse


def arg_parsing() -> Dict:
    """ Parse all arguments variable using the argparse module
        It doesn't take any args and return dict of all the configuration
        variable given in the config file or empty dict if invalid args, or 
        if failed to open the file
    """

    config_variables = {}
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('config_file', help='Path to configuration file')
        args = parser.parse_args()
        with open(args.config_file, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                key, value = line.split("=", 1)
                config_variables[key] = value
    except Exception:
        print(f"can't open file {args.config_file}, no such file or directory")
    return config_variables


print(arg_parsing())
print("test_git")
