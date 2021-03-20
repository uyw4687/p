from copy import deepcopy

def parse_flag_rules(flag_rules, flag_rule_dict, flag_used_template):
    for flag_rule in flag_rules:
        flag_name, flag_argument_type = flag_rule.split()
        flag_rule_dict[flag_name] = flag_argument_type
        
        flag_used_template[flag_name] = False

def check_command(cmd, program, flag_rule_dict, flag_used_template, arg_types_wo_null):
    # split command by whitespaces
    cmd_chunks = cmd.split()
    
    # if the command doesn't start with the program name
    if cmd_chunks[0] != program:
        return False

    # current flag that is being processed
    # False if a flag is not found yet
    #                 or already verified for correctness
    curr_flag = ''

    flag_used = deepcopy(flag_used_template)

    # answer for current command
    good = True
    
    # if curr_flag in ['NUMBERS', 'STRINGS']
    #   True if no more arguments are expected
    #   False if more arguments are expected
    # else
    #   always True
    ended = True

    len_cmd_chunks = len(cmd_chunks)

    i = 1
    while i < len_cmd_chunks:

        # current chunk to process
        curr_chunk = cmd_chunks[i]

        # if current flag is empty, expect a flag
        if curr_flag=='':

            curr_flag_argument_type = flag_rule_dict.get(curr_chunk)
            # invalid flag
            if curr_flag_argument_type == None:
                good = False
                break
            
            if flag_used[curr_chunk]:
                good = False
                break
            flag_used[curr_chunk] = True

            # if an argument is needed
            if curr_flag_argument_type in arg_types_wo_null:
                # store the current flag to expect an argument in the next loop 
                curr_flag = curr_chunk
        
        # expect an argument
        else:
            if curr_flag_argument_type == 'NUMBER':
                if not curr_chunk.isnumeric():
                    good = False
                    break

            elif curr_flag_argument_type == 'STRING':
                if not curr_chunk.isalpha():
                    good = False
                    break

            elif curr_flag_argument_type == 'NUMBERS':
                if not curr_chunk.isnumeric():
                    good = False
                    break

                # check the next chunk in advance
                # to expect further arguments or not
                if (i+1)<len_cmd_chunks:
                    if cmd_chunks[i+1].startswith('-'):
                        ended = True
                    else:
                        ended = False
                else:
                    ended = True

            # for extendability
            elif curr_flag_argument_type == 'STRINGS':
                if not curr_chunk.isalpha():
                    good = False
                    break

                # check the next chunk in advance
                # to expect further arguments or not
                if (i+1)<len_cmd_chunks:
                    if cmd_chunks[i+1].startswith('-'):
                        ended = True
                    else:
                        ended = False
                else:
                    ended = True

            # if no more arguments are expected
            # make it an empty string to expect a flag or EOS in the next loop
            if ended:
                curr_flag = ''
        
        i += 1

    # if the final flag couln't get an argument
    if good and (curr_flag != ''):
        good = False
    
    return good

def solution(program, flag_rules, commands):

    # stores the flag rules in dictionary form
    flag_rule_dict = {}
    # template dictionary which will store 'flag_name: boolean'
    # where boolean is True if the flag is used in a command
    #                  False if the flag is not used yet
    flag_used_template = {}
    parse_flag_rules(flag_rules, flag_rule_dict, flag_used_template)

    # stores the answer
    answer = []

    # argument types without null
    arg_types_wo_null = ['NUMBER', 'STRING','NUMBERS','STRINGS']

    # check if each command is valid
    for cmd in commands:
        result = check_command(cmd, program, flag_rule_dict, flag_used_template, arg_types_wo_null)
        answer.append(result)

    return answer