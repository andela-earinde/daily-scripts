#! /usr/bin/ruby

class TruthTable
    def render(var_count)
        puts var_count
    end
end

var_count = ARGV[0]
table_instance = TruthTable.new
table_instance.render(var_count)
