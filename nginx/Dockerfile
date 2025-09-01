FROM nginx:alpine

# Удаляем дефолтный конфиг
RUN rm /etc/nginx/conf.d/default.conf

# Копируем наш конфиг
COPY nginx.conf /etc/nginx/nginx.conf

# Копируем статику если нужно
COPY html/ /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]