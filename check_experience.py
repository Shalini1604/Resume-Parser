def experience(res_dct,condition,field):
    if '>' in condition:
                            if ">=" in condition: 
                                ndeg=condition.replace(">=", '').strip()
                                print(ndeg)
                                if ndeg.isdigit():
                                    if((res_dct["total_exp"].strip())>=ndeg):
                                        return True
                                else:
                                    print("Enter valid input")
                            else:
                                ndeg=condition.replace('>', '').strip()
                                if ndeg.isdigit():
                                    if((res_dct["total_exp"].strip())>ndeg):
                                        return True
                                else:
                                    print(" Enter valid input ")
    elif '<' in condition: 
                            if "<=" in condition: 
                                ndeg=condition.replace("<=", '').strip()          #string immutable in python
                                if ndeg.isdigit():
                                    if((res_dct["total_exp"].strip())<=ndeg):
                                        return True
                                else:
                                    print(" Enter valid input ")
                            else:
                                ndeg=condition.replace('<', '').strip()
                                if ndeg.isdigit():
                                    if((res_dct["total_exp"].strip())<ndeg):
                                        return True
                                else:
                                    print(" Enter valid input ")
    elif '=' in condition: 
                            ndeg=condition.replace('=', '').strip()
                            if ndeg.isdigit():
                                if((res_dct["total_exp"].strip())==ndeg):
                                    return True
                            else:
                                print(" Enter valid input ")
                        
    else:
        print(" Invalid input for experience ")