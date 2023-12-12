#!/usr/bin/env python3
import re
import sys


CACHE = {}
def count_valid_strings(template:str, sections: [], n_in_current_sec: int) -> int:
    global CACHE
    key = (template, n_in_current_sec, tuple(sections))
    if key not in CACHE:
        CACHE[key] = count_valid_strings_helper(template, sections, n_in_current_sec)
    return CACHE[key]
    
def count_valid_strings_helper(template:str, sections: [], n_in_current_sec: int) -> int:
    if template == "":
        if len(sections) == 0 or (len(sections) == 1 and n_in_current_sec == sections[0]):
            return 1
        return 0
    if n_in_current_sec == 0: # not in a block of '#''
        if template[0] == '.':
            return count_valid_strings(template[1:], sections, 0)
        elif template[0] == '#':
            if len(sections) == 0:
                return 0 
            return count_valid_strings(template[1:], sections, 1)
        else: 
            # It's a '?'
            result = count_valid_strings(template[1:], sections, 0) # Choose a '.'
            if len(sections) > 0:
                result += count_valid_strings(template[1:], sections, 1) # Choose a '#'
            return result 
        assert False, "Sould be unreachable"
    
    # We're in a block now
    if template[0] == '.':
        if n_in_current_sec == sections[0]:
            return count_valid_strings(template[1:], sections[1:], 0) # Look for new blocks
        return 0 
    elif template[0] == '#':
        assert len(sections) > 0
        if n_in_current_sec + 1 > sections[0]:
            return 0 # This section would be too long
        return count_valid_strings(template[1:], sections, n_in_current_sec+1)
    else: 
        # It's a ?
        if n_in_current_sec == sections[0]: # have to choose a '.'
            return count_valid_strings(template[1:], sections[1:], 0)
        assert n_in_current_sec < sections[0]
        return count_valid_strings(template[1:], sections, n_in_current_sec+1) # Have to hoose a '#'
    
    assert False, "Should be unreachable"
        
answer = 0
with open(sys.argv[1], 'r') as infile:
    lines = [l.strip() for l in infile]
    
for l in lines:
    pattern, numbers = l.split(' ')
    sections = [int(n) for n in numbers.split(',')]
    CACHE = {}
    n_possible = count_valid_strings(pattern, sections, 0)
    # print(l, n_possible)
    answer += n_possible

print("Part 1", answer)

answer = 0
for l in lines:
    pattern, numbers = l.split(' ')
    sections = [int(n) for n in numbers.split(',')]
    new_sections = sections * 5
    new_pattern = f"{pattern}?{pattern}?{pattern}?{pattern}?{pattern}"
    CACHE = {}
    n_possible = count_valid_strings(new_pattern, new_sections, 0)
    # print(new_pattern, new_sections, n_possible)
    answer += n_possible
    
print("Part 2", answer)