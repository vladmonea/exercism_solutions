package airportrobot

import "fmt"

// Write your code here.
// This exercise does not have tests for each individual task.
// Try to solve all the tasks first before running the tests.

type Greeter interface {
	LanguageName() string
	SayHello(name string) string
}

func SayHello(name string, greeter Greeter) string {
	var message string
	language := greeter.LanguageName()
	message = fmt.Sprintf("I can speak %s: %s", language, greeter.SayHello(name))
	return message
}

type Italian struct {
	name string
}

func (it Italian) LanguageName() string {
	return "Italian"
}

func (it Italian) SayHello(name string) string {
	return fmt.Sprintf("Ciao %s!", name)
}

type Portuguese struct {
	name string
}

func (por Portuguese) LanguageName() string {
	return "Portuguese"
}

func (por Portuguese) SayHello(name string) string {
	return fmt.Sprintf("Olá %s!", name)
}
