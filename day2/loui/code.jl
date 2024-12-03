
open("input.txt", "r") do file
    lines = readlines(file)
    data = [parse.(Int64, split(line)) for line in lines]
    # println(data)

    assending_matrix = [row for row in data if row == sort(row)]
    descending_matrix = [row for row in data if row == sort(row, rev=true)]
    
    # matrix that includes only truly assending and descending rows of the data set
    combined_matrix = vcat(assending_matrix, descending_matrix)
    
    
end
