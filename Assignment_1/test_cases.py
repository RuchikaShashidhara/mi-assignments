from Assignment1 import *

# binary decision
def test_case_1():
    fever = 'no,yes,yes,yes,yes,no,yes,yes,no,yes,no,no,no,yes'.split(',')
    cough = 'no,yes,yes,no,yes,yes,no,no,yes,yes,yes,yes,yes,yes'.split(',')
    breathe_issues = 'no,yes,no,yes,yes,no,yes,yes,yes,no,no,yes,yes,no'.split(',')
    infected = 'no,yes,no,yes,yes,no,yes,yes,yes,yes,no,no,yes,no'.split(',')

    fever = ['no','no']
    cough = ['no','no']
    breathe_issues = ['no','no']
    infected = ['yes','no']

    dataset ={'fever':fever,'cough':cough,'breathe_issues':breathe_issues,'infected':infected}
    df = pd.DataFrame(dataset,columns=['fever','cough','breathe_issues','infected'])
    print(df)

    print("Entropy: ",get_entropy_of_dataset(df))

    print("\nEntropy of attributes: ")
    for i in ['fever','cough','breathe_issues']:
        print(i,get_entropy_of_attribute(df,i))
        
    print("\nInformation gain of attributes: ")
    for i in ['fever','cough','breathe_issues']:
        print(i,get_information_gain(df,i))
    
    print("\nSelected attribute: ",get_selected_attribute(df))

# multi-valued decision
def test_case_2():
    quality = 'good,good,bad,bad,okay,okay,good,okay'.split(',')
    subject = 'interesting,boring,interesting,boring,interesting,boring,medium,medium'.split(',')
    listen = 'definitely,maybe,maybe,no_way,definitely,maybe,definitely,no_way'.split(',')

    dataset ={'quality':quality,'subject':subject,'listen':listen}
    df = pd.DataFrame(dataset,columns=['quality','subject','listen'])
    print(df)

    print("Entropy: ",get_entropy_of_dataset(df))

    print("\nEntropy of attributes: ")
    for i in ['quality','subject']:
        print(i,get_entropy_of_attribute(df,i))
        
    print("\nInformation gain of attributes: ")
    for i in ['quality','subject']:
        print(i,get_information_gain(df,i))
    
    print("\nSelected attribute: ",get_selected_attribute(df))

# empty df + attribute missing case
def test_case_3():
    dataset = {}
    df = pd.DataFrame(dataset,columns=[])
    print(df)

    print("Entropy: ",get_entropy_of_dataset(df))

    print("\nEntropy of attributes: ")
    for i in ['quality','subject']:
        print(i,get_entropy_of_attribute(df,i))
        
    print("\nInformation gain of attributes: ")
    for i in ['quality','subject']:
        print(i,get_information_gain(df,i))
    
    print("\nSelected attribute: ",get_selected_attribute(df))

# df with only decision column
def test_case_4():

    infected = 'no,yes,no,yes,yes,no,yes,yes'.split(',')
    dataset = {'infected':infected}
    df = pd.DataFrame(dataset,columns=['infected'])
    print(df)

    print("Entropy: ",get_entropy_of_dataset(df))

    print("\nEntropy of attributes: ")
    for i in ['quality','subject']:
        print(i,get_entropy_of_attribute(df,i))
        
    print("\nInformation gain of attributes: ")
    for i in ['quality','subject']:
        print(i,get_information_gain(df,i))
    
    print("\nSelected attribute: ",get_selected_attribute(df))

if __name__=="__main__":
    print('\nTEST CASE 1:')
    test_case_1()
    print('\nTEST CASE 2:')
    test_case_2()
    print('\nTEST CASE 3:')
    test_case_3()
    print('\nTEST CASE 4:')
    test_case_4()
