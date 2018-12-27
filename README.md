# @pastor_brown

The [twitch.tv](https://twitch.tv) bot for the Harvest Moon speedrunning community.

## Commands

All commands start with `+` symbol and are case-insensitive.

1. `StartRace`: Starts a new race, will erase existing bets and open new betting
1. `Bet|Horse|Dog [NUMBER]`: Any of these words followed by a number places a bet for that user. Only 1 bet per user
1. `EndBetting`: Closes the race and no new bets are allowed
1. `Winners [NUMBER]`: Announces all bets who matched the provided number

## Getting Started

```
pipenv install
pipenv run python runner.py
```
