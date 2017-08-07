print('Escape from Cave Terror!')
action_input = input('Action: ')
if action_input == 'n':
    print("Go North!")
elif action_input == 's':
    print("Go South!")
elif action_input == 'e':
    print("Go East")
elif action_input == 'w':
    print("Go West")
else:
    print("Invalid option; Choose one from n,s,e,w!")
