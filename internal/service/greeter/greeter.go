package greeter

import (
	"context"
	v1 "kratos-tutorial/api/greeter/v1"
	biz "kratos-tutorial/internal/biz/greeter"
)

type GreeterService struct {
	v1.UnimplementedGreeterServer

	usecase *biz.GreeterUsecase
}

func NewGreeterService(usecase *biz.GreeterUsecase) *GreeterService {
	return &GreeterService{usecase: usecase}
}

func (gs *GreeterService) Greet(ctx context.Context, request *v1.GreetRequest) (*v1.GreetReply, error) {
	return &v1.GreetReply{Message: gs.usecase.Greet(request.Name)}, nil
}
