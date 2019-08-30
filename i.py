from fg import Figure, DynFig, ColorFig, ColDifFig

# figure = Figure('blue', 10, 90, 200)
# figure.render(10)

# figure = DynFig('silver', 10, 90, 200, 10)
# figure.render(20)

# figure = ColorFig('silver', 10, 90, 200, ['red', 'green', 'yellow', 'purple', 'blue', 'silver', 're'])
# figure.render(20)

figure = ColDifFig('silver', 10, 90, 200, ['red', 'green', 'yellow', 'purple', 'blue', 'silver', 'red'], 5, 1)
figure.render(46)
