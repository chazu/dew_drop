import matplotlib.pyplot as pyplot

import component
import item

test_item = component.Component({
        'longevity': 1000,
        'durability_coefficient': 1,
        'unreliability_threshold': 0.35,
        'failure_threshold': 0.2,
        'inaccuracy_rating': 0.02,
        'inaccuracy_growth_factor': 0.35
        })

longevity_values = []

inaccuracy_pct_values = []

while test_item.current_longevity > 0:
    longevity_values.append(test_item.current_longevity)
    inaccuracy_pct_values.append(test_item.get_inaccuracy_percentage())
    test_item.update_durability()
    print str(test_item.current_longevity)

pyplot.plot(inaccuracy_pct_values, longevity_values)
print(inaccuracy_pct_values)
print(longevity_values)
pyplot.savefig('chart.png')
pyplot.show()
