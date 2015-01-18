#! /usr/bin/ruby

class TruthTable
    
    def render(var_count=1)
        (2**var_count).times do |i|
            puts i.to_s(2).rjust(var_count, '0').gsub('0', 'F ').gsub('1', 'T ')
        end
    end
end

count = ARGV[0].to_i
truth_table = TruthTable.new
truth_table.render(count)
