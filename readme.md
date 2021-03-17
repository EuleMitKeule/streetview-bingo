[![api-test](https://github.com/euleGIT/streetview-bingo/actions/workflows/api-test.yml/badge.svg?branch=master&event=push)](https://github.com/euleGIT/streetview-bingo/actions/workflows/api-test.yml)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=euleGIT_streetview-bingo&metric=coverage)](https://sonarcloud.io/dashboard?id=euleGIT_streetview-bingo)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=euleGIT_streetview-bingo&metric=bugs)](https://sonarcloud.io/dashboard?id=euleGIT_streetview-bingo)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=euleGIT_streetview-bingo&metric=code_smells)](https://sonarcloud.io/dashboard?id=euleGIT_streetview-bingo)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=euleGIT_streetview-bingo&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=euleGIT_streetview-bingo)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=euleGIT_streetview-bingo&metric=ncloc)](https://sonarcloud.io/dashboard?id=euleGIT_streetview-bingo)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=euleGIT_streetview-bingo&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=euleGIT_streetview-bingo)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=euleGIT_streetview-bingo&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=euleGIT_streetview-bingo)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=euleGIT_streetview-bingo&metric=security_rating)](https://sonarcloud.io/dashboard?id=euleGIT_streetview-bingo)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=euleGIT_streetview-bingo&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=euleGIT_streetview-bingo)

# Introduction

streetview-bingo is inspired by [Geowizards Videos](https://www.youtube.com/watch?v=3B72lu2WdEo). 
This application adopts this idea and provides a platform to play this game with your friends.

The concept is simple: One of the players comes up with a list of things that can be found on Google Street View. The players job is it to find those things as quick as possible on Google Street View, and then tell the first player, who is acting as a moderator and verifies it for you.

Street View Bingo can be played in person, using multiple devices, or via the internet, while sharing your screen with the moderator. Discord for example has a feature to let multiple users share their screen at the same time, which enables the moderator to quickly verify the findings.

# Features

## What this application does
* Functionality to create a lobby. One user creates a lobby, the other users can join the it using a generated lobby-token.
* Set-up the game: The lobby-owner can create a game and assign one of the players as moderator for this round.
* The moderator then configures the game and selects the things that can be found. The application includes a list of words that can be used as a preset, but it is also encouraged to come up with your own words.
* Track the progress of the game: After starting the game, the players have an overview over how many things the other players have found so far. The moderator verifies the things for each player and marks them on the board.

## What this application does not do
* It does not include a framework for automatic verification. The moderator has to look at the user's screen, either in person, or via desktop sharing applications.

# Getting Started

## Prerequisite

You need Python and Node installed on your machine to run this application. Furthermore, all dependencies defined in ``requirements.txt`` should be installed.

## How to deploy

### Development

Start the frontend by first running the OpenAPI-Generator, then start the application using ``ng serve``. The UI should run on port 4200.

### Production

The flask server is set up to serve the Angular build files. Run ``ng build`` to generate them. The UI should be available at the root path of the flask server.

