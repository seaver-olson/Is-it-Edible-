import pandas as pd

df = pd.read_csv('mushrooms.csv')

def user_input():
    cap_color = input('What is the cap color? brown=n,buff=b,cinnamon=c,gray=g,green=r,pink=p,purple=u,red=e,white=w,yellow=y')
    cap_shape = input('What is the cap shape? bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s')
    odor = input('What is the odor? ')
    gill_color = input('What is the gill color? ')
    gill_size = input('What is the gill size? ')
    stalk_shape = input('What is the stalk shape? ')
    description = {'cap-color': cap_color, 'cap-shape': cap_shape, 'odor': odor, 'gill-color': gill_color, 'gill-size': gill_size, 'stalk-shape': stalk_shape}
    return description

def shrink(description, df):
    '''
    shrinks down possible rows
    '''
    df = df[df['cap-color'] == description['cap-color']]
    df = df[df['cap-shape'] == description['cap-shape']]
    df = df[df['odor'] == description['odor']]
    df = df[df['gill-color'] == description['gill-color']]
    df = df[df['gill-size'] == description['gill-size']]
    df = df[df['stalk-shape'] == description['stalk-shape']]
    return df
    
def isPoisonous(df):
    '''
    returns the percent chance of being poisonous
    '''
    poisonous = df[df['class'] == 'p']
    edible = df[df['class'] == 'e']
    return len(poisonous) / (len(poisonous) + len(edible))

def main():
    description = user_input()
    df = shrink(description, df)
    print(isPoisonous(df))
    
