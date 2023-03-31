{% extends "base.html" %}
{% load static %}
{% block title %}
  Анфиса для друзей. Каталог мороженого
{% endblock %}
{% block content %}
  <h1 class="pb-2 mb-0">Каталог мороженого</h1>
          <div class="row">

          <!-- Начинается перебор мороженого  в цикле -->
              <!-- Карточка товара 0 -->

              <div class="col-6 col-md-4 my-1">
                <div class="card">
                  <img
                    class="img-fluid card-img-top"
                    height="400" width="300"
                    src="{% static 'img/image-holder.png' %}"
                  >
                  <div class="card-body">
                    <h5 class="card-title">Классический пломбир</h5>
                    <p class="card-text">
                      <!-- Описание обрезано до первых 10ти слов -->
                      Настоящее мороженое, для истинных ценителей вкуса. Если на столе появляется ...
                    </p>
                    <!-- Ссылка на товар 0 -->
                    <a class="mt-3 regular-link" href="{% include 'ice_cream/detail.html' %}">
                      Подробнее -->
                    </a>
                  </div>
                </div>
              </div>
              <!-- Конец карточки товара 0 -->
              <!-- Карточка товара 1 -->
              <div class="col-6 col-md-4 my-1">
                <div class="card">
                  <img
                    class="img-fluid card-img-top"
                    height="400" width="300"
                    src="{% static 'img/image-holder.png' %}"
                  >
                  <div class="card-body">
                    <h5 class="card-title">Мороженое с кузнечиками</h5>
                    <p class="card-text">
                      <!-- Описание обрезано до первых 10ти слов -->
                      В колумбийском стиле: мороженое с добавлением настоящих карамелизованных кузнечиков.
                    </p>
                    <!-- Ссылка на товар 1 -->
                    <a class="mt-3 regular-link" href="{% include 'ice_cream/detail.html' %}">
                      Подробнее -->
                    </a>
                  </div>
                </div>
              </div>
              <!-- Конец карточки товара 1 -->
              <!-- Карточка товара 2 -->
              <div class="col-6 col-md-4 my-1">
                <div class="card">
                  <img
                    class="img-fluid card-img-top"
                    height="400" width="300"
                    src="{% static 'img/image-holder.png' %}"
                  >
                  <div class="card-body">
                    <h5 class="card-title">Мороженое со вкусом сыра чеддер</h5>
                    <p class="card-text">
                      <!-- Описание обрезано до первых 10ти слов -->
                      Вкус настоящего сыра в вафельном стаканчике.
                    </p>
                    <!-- Ссылка на товар 2 -->
                    <a class="mt-3 regular-link" href="{% include 'ice_cream/detail.html' %}">
                      Подробнее -->
                    </a>
                  </div>
                </div>
              </div>
              <!-- Конец карточки товара 2 -->
            <!-- Конец цикла  -->

          </div>
{% endblock %}