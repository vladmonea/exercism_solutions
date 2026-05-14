package parsinglogfiles

import (
	"regexp"
)

func IsValidLine(text string) bool {
	if len(text) < 5 {
		return false
	}
	tag, err := regexp.Compile(`^\[(ERR|INF|WRN|DBG)\].*`)
	if err != nil {
		return false
	}
	match := tag.MatchString(text)
	if match {
		return true
	} else {
		return false
	}
}

func SplitLogLine(text string) []string {
	if len(text) < 1 {
		return []string{""}
	}
	re, err := regexp.Compile(`<\W*?>`)
	if err != nil {
		return []string{""}
	}
	return re.Split(text, -1)
}

func CountQuotedPasswords(lines []string) int {
	if len(lines) < 1 {
		return 0
	}
	re, err := regexp.Compile(`(?i).*\".*password.*\".*`)
	if err != nil {
		return -1
	}
	counter := 0
	for i := range lines {
		match := re.MatchString(lines[i])
		if match {
			counter++
		}
	}
	return counter
}

func RemoveEndOfLineText(text string) string {
	if len(text) < 1 {
		return ""
	}

	re, err := regexp.Compile(`(end-of-line\d+)`)
	if err != nil {
		return ""
	}
	clean := re.ReplaceAllString(text, "")
	return clean
}

func TagWithUserName(lines []string) []string {
	if len(lines) < 1 {
		return []string{""}
	}
	re, err := regexp.Compile(`User\s+(\w+)`)
	if err != nil {
		return []string{""}
	}
	output := make([]string, 0)
	for i := range lines {
		if IsValidLine(lines[i]) {
			found := re.FindStringSubmatch(lines[i])
			if len(found) < 1 {
				output = append(output, lines[i])
			} else {
				toAdd := "[USR] " + found[1] + " " + lines[i]
				output = append(output, toAdd)
			}
		} else {
			output[i] = lines[i]
		}
	}
	return output
}
