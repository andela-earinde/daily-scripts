#! /usr/bin/ruby

class Towers

    def move(n, fro, to, spare)
        if n <= 1
            print_move(fro, to)
        else
            move(n - 1, fro, spare, to)
            move(1, fro, to, spare)
            move(n - 1, spare, to, fro)
        end
    end

    private
    def print_move(fro, to)
        puts "Move peg from #{fro} to #{to}."
    end
end

towers_of_hanoi = Towers.new
ring_count = ARGV[0].to_i
towers_of_hanoi.move(ring_count, 'A', 'B', 'C')

