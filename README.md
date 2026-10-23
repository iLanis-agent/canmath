# Can Math

Event soda can carton, week, cost and time arithmetic. The 468 cans at 24 cans a carton take 20 cartons, the last carton holding 12 cans.

## Named constants

None. Every number is the owner's own entry.

## What it computes

- **The cartons truth** - the cans (1 to 1000000) divided by the cans a carton (1 to 1000), rounded up, with what the last carton holds.
- **The weeks truth** - the cans divided by the cans used a week (1 to 100000), with the cans left for the next week.
- **The cost truth** - the cartons (1 to 100000) times the carton price ($0.01 to $999.99) to the cent, and spread over the cans, half rounded up.
- **The time truth** - the cans divided by the cans caned a minute (1 to 100), rounded up, in minutes and in hours and minutes.

## Boundary

Arithmetic only. Counting applied as written. It has not seen any can, carton or cooler and does not know whether cans will really arrive cold, a supplier will run out or a price will hold, and it gives no verdict that a carton is worth its price or a can is right for an event. Every number is the owner's own entry.

## Files

- `index.html` - landing page with the boundary and starting examples.
- `app.html` - the calculator; every carton recomputes on each keystroke.
- `engine.js` - the four truths, shared by the page and the tests.
- `oracle.py` - an independent Python re-implementation; writes `expected.json`.
- `test.js` - runs the engine against `expected.json` (99 cases, 20 error cases).

## Tests

```
python3 oracle.py
node test.js
```
