# Poker-Optimization

This repository contains the implementation of the Article [Estimating the strengh of poker hands by integer liner programming techniques](https://github.com/RaulBritto/Poker-Optimization/blob/master/docs/CEJOR.pdf).
The code is divided into two parts: the preprocessing using Python and the optmization process using Julia and JuMP.

## Preprocessing

The preprocessing was done using the follow references: 
[How to Calculate Poker Probabilities in Python](https://towardsdatascience.com/how-to-calculate-poker-probabilities-in-python-75238c61421e)
by Thársis Souza; the [Poker Python module](https://pypi.org/project/poker/) (a Python framework for poker related operations) and 
[Holdem Calculator](https://github.com/ktseng/holdem_calc) (a library that calculates the probability that a certain Texas Hold'em hand will win).

The **analyze function** in main.py simulates a random flop, extracting a set of features describe in [article](https://github.com/RaulBritto/Poker-Optimization/blob/master/docs/CEJOR.pdf) and calculating the hero's equity against a villan range defined as input. 
By default **analyze function** simulates all 19600 posibilities of flop, but it's possible to define the number of flop simulation defining the *iterations* argument in **analyze funtion**.
It's possible call the **analyze function** from prompt with the command bellow:

```console
python src/main.py --hand KhKc --range '22+ AKs' -n 2
```
* --hand defines the hero hand 
* --range deines the villan range
* -n defines the number of flop simulation

## Optimization

The optimization is done using Julia and [JuMP](https://jump.dev/JuMP.jl/v0.19.0/index.html).
The optimization code and model could be find in the file **main.jl**

The first part of code uses the [PyCall](https://github.com/JuliaPy/PyCall.jl) package to call the preprocessing code done in Python.
After call the **analyze function** in Python maybe could be helpful save the return values using [JLD](https://github.com/JuliaIO/JLD.jl) package. 

The following command save Julia variables into a file:
```julia
using JLD
save("myfile.jld", "features", b, "probabilities", e)
```

To read a file wiht variables use the command bellow:
```julia
using JLD
d = load("myfile.jld")
```

