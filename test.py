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
import sys 
import random


def arg_parsing() -> Dict:
    """ Parse all arguments variable using the argparse module
        It doesn't take any args and return dict of all the configuration
        variable given in the config file or empty dict if invalid args, or 
        if failed to open the file
    """
    config_variables: Dict = {}

    if len(sys.argv) < 2:
        print("Error: No configuration provided."
              "\nUsgae: python3 a_maze_ing.py <config.txt>")
        return config_variables

    if len(sys.argv) > 2:
        print("Warning: Too many arguments provided."
              "Only the first one will be used\n")

    # File-level errors handling:
    # File not found, Cannot open file, No read permission
    config_file = sys.argv[1]
    try:
        with open(config_file, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                config_variables[line] = line
                # key, value = line.split("=", 1)
                # config_variables[key] = value
    except FileNotFoundError:
        print(f"[Error]: Cannot open file '{config_file}'\n"
               "Error detail: File not found")
        return config_variables
    except PermissionError:
        print(f"[Error]: Cannot open file '{config_file}'\n"
               "Error detail: Permission error")
        return config_variables
    except Exception as e:
        print(f"Unexpected error: {e}")

    # argument validation
    return config_variables


print(arg_parsing())
