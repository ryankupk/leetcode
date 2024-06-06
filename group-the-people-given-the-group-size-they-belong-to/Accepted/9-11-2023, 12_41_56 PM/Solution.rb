// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to

# @param {Integer[]} group_sizes
# @return {Integer[][]}
def group_the_people(group_sizes)
    groups = []
    groups_hash = {} # group_size => [ [ group_one ], [ group_two ] ]
    """
    {
        2 => [ [0, 5] ],
        1 => [ [1] ],
        3 => [ [2, 3, 4] ]
    }
    """
    group_sizes.each_with_index do | group_size, person_id | 
        if groups_hash.has_key? group_size

            groups_full = true
            groups_hash[group_size].each do | groups_list |

                if groups_list.size != group_size
                    groups_list << person_id
                    groups_full = false
                end

            end
            
            if groups_full == true

                groups_hash[group_size] << [person_id]

            end
        else

            groups_hash[group_size] = [[person_id]]

        end
    end

    groups_hash.each do | group_size, groups_of_group_size |
        groups_of_group_size.each do | group |
            groups << group
        end
    end
    return groups
end