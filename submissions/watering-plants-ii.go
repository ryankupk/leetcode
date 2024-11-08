/*
 * @lc app=leetcode id=2105 lang=golang
 *
 * [2105] Watering Plants II
 */

// @lc code=start
func waterPlant(refills, current, capacity, plantNeeds int) (int, int) {
	if current >= plantNeeds {
		current -= plantNeeds
	} else if current < plantNeeds {
		refills++
		current = capacity - plantNeeds
	}

	return refills, current
}

func minimumRefill(plants []int, capacityA int, capacityB int) int {

	aRefills, bRefills := 0, 0
	a, b := 0, len(plants)-1
	aCurrent, bCurrent := capacityA, capacityB

	for {
		if a == b {
			if aCurrent > bCurrent {
				aRefills, aCurrent = waterPlant(aRefills, aCurrent, capacityA, plants[a]) // a water
				a++
			} else if aCurrent < bCurrent {
				bRefills, bCurrent = waterPlant(bRefills, bCurrent, capacityB, plants[b]) // b water
				b--
			} else {
				aRefills, aCurrent = waterPlant(aRefills, aCurrent, capacityA, plants[a]) // a water
				a++
			}
			break
		} else if b < a {
			break
		}

		aRefills, aCurrent = waterPlant(aRefills, aCurrent, capacityA, plants[a]) // a water
		a++
		bRefills, bCurrent = waterPlant(bRefills, bCurrent, capacityB, plants[b]) // b water
		b--
	}
	return aRefills + bRefills
}

// @lc code=end

