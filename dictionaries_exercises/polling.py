# Polling 6.6

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}")

# New poll takers loop
    
new_poll_takers = ['don', 'sarah', 'billy']

for name in new_poll_takers:
    if name in favorite_languages:
        print("\nThanks for responding!")
    else:
        print("\nPlease take the poll")