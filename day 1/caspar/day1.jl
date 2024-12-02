function read_data(filename)
	numbers1 = Int[]
	numbers2 = Int[]
	open(filename) do file
		for line in eachline(file)
            n1, n2 = split(line, "   ")
			append!(numbers1, parse(Int, n1))
			append!(numbers2, parse(Int, n2))
		end 
	end
	numbers1, numbers2
end
n1, n2 = read_data("inputfile")
sum(abs.(sort(n1) .- sort(n2)))
simscore = 0
for a in n1
    i = 0
    for b in n2
        if a == b
            i += 1
        end
    end
    simscore += a*i
end
simscore