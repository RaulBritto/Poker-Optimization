using PyCall

push!(pyimport("sys")["path"], pwd()* "/src");

fe = pyimport("main")
poker = pyimport("poker")
re  =  pyimport("rangeEquity")
heroHand = poker.Combo("JcJh")
flop = ["Kh", "Jd", "Th"]
villan_range =  re.RS


b, e = fe.analyze(heroHand, villan_range, 10)
m = size(b)[1]

using JuMP
using GLPK

model = Model(GLPK.Optimizer)

N = 20
@variable(model, ε[1:m] >= 0)
@variable(model, y[1:73], Bin)
@variable(model, x[1:73])


@constraint(model, sum(y[i] for i in 1:73)  <= N)
for i = 1:m
    @constraint(model, sum(b[i,j]*x[j] for j in 1:73) <= e[i]+ε[i])
    @constraint(model, sum(b[i,j]*x[j] for j in 1:73) >= e[i]-ε[i])
end
    
for i in 1:73
    @constraint(model, [i = 1:73], x[i] >= -y[i])
    @constraint(model, [i = 1:73], x[i] <= y[i])
end

@objective(model, Min, sum(ε[i] for i in 1:m)/m)

JuMP.optimize!(model) # Old syntax: status = JuMP.solve(model)
JuMP.objective_value(model)