package proto

type Request struct {
	// само число, которое будем проверять на кратность тройке
	Number string `json:"number"`
	// идентификатор запроса
	Ident string `json:"ident"`
}

type Response struct {
	Status string `json:"status"`
	Ident string `json:"ident"`
}
