quotation = { 'Carl Sagan'      : 'Somewhere, something incredible is waiting to be known.',
              'Richard Feynman' : 'The first principle is that you must not fool yourself and you are the easiest person to fool.',
              'Isaac Asimov'    : 'Am I trying to find God? Well, God is smarter than me, so let him find me.',
              'Walt Disney'     : 'Laughter is timeless, imagination has no age, and dreams are forever.',
              'Mahatma Gandhi'  : ' Live as if you were to die tomorrow. Learn as if you were to live forever.',
              'the Terminator'  : "I'll be back.",
              'Lao Tzu'         : 'When I let go of what I am, I become what I might be.',
              'Jim Carrey'      : "Good morning! And in case I don't see you: good afternoon, good evening and good night.",
              'Isaac Newton'    : 'We build too many walls and not enough bridges.',
              'Mark Twain'      : "It's not the size of the dog in the flight, it's the size of the fligt in the dog."
    }

running = True

while running:
 i = raw_input('Quotation of the Day:')
 print '%%%%%%%%%%%%%%%%%%% Quotation of the Day %%%%%%%%%%%%%%%%%%%%%%%%%%','\n','%', quotation[i], '%','\n', '%', '--', i, '%', '\n', '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
 if  i != raw_input('Quotation of the Day:'):
   print 'Get Out'
