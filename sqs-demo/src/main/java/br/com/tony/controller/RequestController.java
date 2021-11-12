package br.com.tony.controller;

import io.micronaut.http.HttpResponse;
import io.micronaut.http.annotation.Body;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.annotation.Post;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Controller(value = "/api")
public class RequestController {

    private static final Logger logger = LoggerFactory.getLogger(RequestController.class.getName());

    @Get
    public HttpResponse<String> get() {
        return HttpResponse.ok("Request recebida");
    }

    @Post
    public void post(@Body String s) {
        logger.info(s);
    }
}
