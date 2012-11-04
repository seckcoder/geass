#!/usr/bin/ruby

class BitField
    attr_reader :size
    include Enumerable

    ELEMENT_WIDTH = 32

    def initialize(size)
        @size = size
        @field = Array.new(((size - 1) / ELEMENT_WIDTH) + 1, 0)
    end

    # Set a bit (1/0)
    def []=(position, value)
        if value == 1
            @field[position / ELEMENT_WIDTH] |= 1 << (position % ELEMENT_WIDTH)
        elsif (@field[position / ELEMENT_WIDTH]) & (1 << (position % ELEMENT_WIDTH)) != 0
            @field[position / ELEMENT_WIDTH] ^= 1 << (position % ELEMENT_WIDTH)
        end
    end

    # Read a bit (1/0)
    def [](position)
        @field[position / ELEMENT_WIDTH] & 1 << (position % ELEMENT_WIDTH) > 0 ? 1 : 0
    end

    # Iterate over each bit
    def each(&block)
        @size.times { |position| yield self[position] }
    end

    # Returns the field as a string like "0101010100111100," etc.
    def to_s
        inject("") { |a, b| a + b.to_s }
    end

    # Returns the total number of bits that are set
    # (The technique used here is about 6 times faster than using each or inject direct on the bitfield)
    def total_set
        @field.inject(0) { |a, byte| a += byte & 1 and byte >>= 1 until byte == 0; a }
    end
end
class BloomFilter
    def initialize(m, k)
        @bitv_size, @hash_size = m, k
        @bitv = BitField.new(@bitv_size)
    end
    def hash_indices(value)
        indices = Array.new
        0.upto(@hash_size-1) do |i|
            indices << (value.hash.abs + i * self.hashpjw(value)) % @bitv_size
        end
        indices
    end
    def hashpjw(s)
        val = 0
        s.each_byte do |c|
            val = (val << 4) + c
            tmp = (val & 0xf0000000)
            if tmp != 0
                val = val ^ ( tmp >> 24)
                val = val ^ tmp
            end
        end
        val
    end
    def insert(value)
        indices = self.hash_indices(value)
        indices.each { |ind| @bitv[ind] = 1 }
    end
    def lookup(value)
        self.hash_indices(value).each do |ind|
            if @bitv[ind] != 1
                return false
            end
        end
        true
    end
end

filter = BloomFilter.new(200000, 3)
filter.insert('haha')
puts filter.lookup('haha')
puts filter.lookup('ahaa')
filter.insert('中国')
puts filter.lookup('中国')
