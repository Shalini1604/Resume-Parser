import check_andor
import check_experience
def check_condition(res_dct,condition,field):
                        if field not in res_dct:
                            return "-1"
                        else:
                            if(field=="total_exp"):
                                val=check_experience.experience(res_dct,condition,field)
                                if val:
                                    return True
                            else:
                                l=condition.lower().split(" ")
                                if len(l)==1:
                                    if l[0].strip() in [i.strip() for i in res_dct[field].lower().split(",")]:
                                        return True
                                    else:
                                        return False
                                #if invalid skills given like and and c++ here and in place of skill not handled
                                for i in range(1,len(l),2):
                                    if l[i]=="and":
                                        temp=check_andor.cond_and(res_dct,field,l[i-1].lower().strip(),l[i+1].lower().strip())
                                        if not temp:
                                            return False
                                    elif l[i]=="or":        #how and or works 
                                        temp=check_andor.cond_or(res_dct,field,l[i-1].lower().strip(),l[i+1].lower().strip())
                                        if not temp:
                                            return False
                                    else:
                                        return "invalid"
                                return True
