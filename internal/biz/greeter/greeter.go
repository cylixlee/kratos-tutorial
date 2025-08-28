package greeter

import "fmt"

type GreeterUsecase struct{}

func NewGreeterUsecase() *GreeterUsecase {
	return &GreeterUsecase{}
}

func (g *GreeterUsecase) Greet(name string) string {
	return fmt.Sprintf("Hello, %s", name)
}
