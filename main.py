# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# UEFA Euro 1988 Final part 1
scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco Van Basten'
goal_0 = 32
goal_1 = 54
scorers = (scorer_1) + ''+ str(goal_0)+'' + (scorer_2) + ''+ str(goal_1)
print(scorers)

report = (f'{scorer_1} scored in the {goal_0}nd minute'\n
{scorer_2} scored in the {goal_1}th minute')

# UEFA Euro 1988 Final part 2
player = 'Adri van Tiggelen'
first_name = player[:player.find('')]
print(first_name)
first_name_len = (len(first_name))
print(first_name_len)

last_name = player[player.find('')+1:]
last_name_len = (len(last_name))
print(last_name_len)

name_short = ((first_name[0]) + '.' + '' + (last_name))
print(name_short)

x = (first_name_len - 1)
chant = (x * (first_name + '!') + (first_name + '!'))
print(chant)

good_chant = chant[-1]!= ''
print(good_chant)



                