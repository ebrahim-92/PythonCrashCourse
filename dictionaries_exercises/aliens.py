# Nesting dictionaries practice

# Make an empty list for storing aliens

aliens = []

# Make 30 aliens

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("....")

# Show how many aliens were created
print(f"Total number of aliens: {len(aliens)}")