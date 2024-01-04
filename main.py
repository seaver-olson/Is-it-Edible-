import pandas as pd


def user_input():
    cap_color = input('What is the cap color? brown=n,buff=b,cinnamon=c,gray=g,green=r,pink=p,purple=u,red=e,white=w,yellow=y')
    cap_shape = input('What is the cap shape? bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s')
    odor = input('What is the odor? almond=a,anise=l,creosote=c,fishy=y,foul=f,musty=m,none=n,pungent=p,spicy=s')
    gill_color = input('What is the gill color? black=k,brown=n,buff=b,chocolate=h,gray=g, green=r,orange=o,pink=p,purple=u,red=e,white=w,yellow=y')
    gill_size = input('What is the gill size? broad=b,narrow=n')
    stalk_shape = input('What is the stalk shape? enlarging=e,tapering=t')
    description = {'cap-color': cap_color, 'cap-shape': cap_shape, 'odor': odor, 'gill-color': gill_color, 'gill-size': gill_size, 'stalk-shape': stalk_shape}
    return description
    
def shrink(description):
    '''
    shrinks down possible rows
    '''
    df = pd.read_csv('mushrooms.csv')
    for key in description:
        df = df[df[key] == description[key]]
    return df

def isPoisonous(df):
    '''
    returns the percent chance of being poisonous
    '''
    poisonous = df[df['class'] == 'p']
    edible = df[df['class'] == 'e']
    try:
        return "percent chance that the mushroom is poisonous: " + str((len(poisonous) / (len(poisonous) + len(edible)))*100)
    except ZeroDivisionError:
        return "No mushrooms found with that description"

def main():
    description = user_input()
    df = shrink(description)
    print(isPoisonous(df))
    

main()
