package gross

// Units stores the Gross Store unit measurements.
func Units() map[string]int {
	units := make(map[string]int)
	units["quarter_of_a_dozen"] = 3
	units["half_of_a_dozen"] = 6
	units["dozen"] = 12
	units["small_gross"] = 120
	units["gross"] = 144
	units["great_gross"] = 1728
	return units
}

// NewBill creates a new bill.
func NewBill() map[string]int {
	return make(map[string]int)
}

// AddItem adds an item to customer bill.
func AddItem(bill, units map[string]int, item, unit string) bool {
	value, unitExists := units[unit]
	if unitExists {
		_, itemExists := bill[item]
		if itemExists {
			bill[item] += value
		} else {
			bill[item] = value
		}
		return true
	}
	return false
}

// RemoveItem removes an item from customer bill.
func RemoveItem(bill, units map[string]int, item, unit string) bool {
	price, itemExists := bill[item]
	value, unitExists := units[unit]
	if itemExists && unitExists {
		if price-value < 0 {
			return false
		} else if price-value == 0 {
			delete(bill, item)
		} else {
			bill[item] -= value
		}
		return true
	}
	return false
}

// GetItem returns the quantity of an item that the customer has in his/her bill.
func GetItem(bill map[string]int, item string) (int, bool) {
	qty, exists := bill[item]
	if exists {
		return qty, true
	}
	return 0, false
}
