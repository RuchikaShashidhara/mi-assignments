from Assignment1 import *

def test_case():
    outlook = 'overcast,overcast,overcast,overcast,rainy,rainy,rainy,rainy,rainy,sunny,sunny,sunny,sunny,sunny'.split(',')
    temp = 'hot,cool,mild,hot,mild,cool,cool,mild,mild,hot,hot,mild,cool,mild'.split(',')
    humidity = 'high,normal,high,normal,high,normal,normal,normal,high,high,high,high,normal,normal'.split(',')
    windy = 'FALSE,TRUE,TRUE,FALSE,FALSE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,FALSE,TRUE'.split(',')
    play = 'yes,yes,yes,yes,yes,yes,no,yes,no,no,no,no,yes,yes'.split(',')
    dataset ={'outlook':outlook,'temp':temp,'humidity':humidity,'windy':windy,'play':play}
    df = pd.DataFrame(dataset,columns=['outlook','temp','humidity','windy','play'])
    try:
        if get_entropy_of_dataset(df) >=0.938 and get_entropy_of_dataset(df)<=0.942:
            print("Test Case 1 for the function get_entropy_of_dataset PASSED")
        else:
            print("Test Case 1 for the function get_entropy_of_dataset FAILED")
    except:
        print("Test Case 1 for the function get_entropy_of_dataset FAILED")

    try:
        if get_entropy_of_attribute(df,'outlook')>=0.691 and get_entropy_of_attribute(df,'outlook')<=0.695 :
            print("Test Case 2 for the function get_entropy_of_attribute PASSED")
        else:
            print("Test Case 2 for the function get_entropy_of_attribute FAILED")

    except:
         print("Test Case 2 for the function get_entropy_of_attribute FAILED")

    try:
        if get_entropy_of_attribute(df,'temp')>=0.908 and get_entropy_of_attribute(df,'temp')<=0.914:
            print("Test Case 3 for the function get_entropy_of_attribute PASSED")
        else:
            print("Test Case 3 for the function get_entropy_of_attribute FAILED")

    except:
        print("Test Case 3 for the function get_entropy_of_attribute FAILED")

    try:
        columns=['outlook','temp','humidity','windy','play']
        ans=get_selected_attribute(df)
        dictionary=ans[0]
        flag=(dictionary['outlook']>=0.244 and dictionary['outlook']<=0.248) and (dictionary['temp']>=0.0292 and dictionary['temp']<=0.0296)and(dictionary['humidity']>=0.150 and dictionary['humidity']<=0.154)and(dictionary['windy']>=0.046and dictionary['windy']<=0.05)and(ans[1]=='outlook')
        if flag:
            print("Test Case 4 for the function get_selected_attribute PASSED")
        else:
            print("Test Case 4 for the function get_selected_attribute FAILED")

    except:
        print("Test Case 4 for the function get_selected_attribute FAILED")



if __name__=="__main__":
	test_case()