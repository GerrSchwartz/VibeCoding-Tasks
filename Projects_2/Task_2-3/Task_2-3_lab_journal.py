user_fio = input ('input your FIO: ')
experiment_date = input ('input experiment date: ')
experiment_name = input ('input experiment name: ')
experiment_results = input ('input experiment results: ')

with open('C:/Users/Chernyx_Aleksandr/journal.txt', 'w', encoding='utf-8') as file:
    file.write ('LAB JOURNAL\n\n')
    file.write (f"Researcher name:\t{user_fio}\nDate:\t{experiment_date}\nExperiment:\t{experiment_name}\n\n")
    file.write (f'Results:\n{experiment_results}')