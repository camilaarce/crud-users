<template>
  <div class="row mt-3">
    <div class="col-md-6 offset-md-3">
      <div class="card">
        <div class="class-header bg-primary text-white text-center p-2">
          Crear usuario
        </div>
        <div class="card-body">
          <form v-on:submit="guardar">
            <div class="input-group mb-3">
              <span class="input-group-text"
                ><i class="fa-solid fa-user"></i
              ></span>
              <input
                type="text"
                v-model="name"
                id="nombre"
                class="form-control"
                maxlength="150"
                placeholder="Nombre del usuario"
                required
              />
            </div>
            <div class="input-group mb-3">
              <span class="input-group-text"
                ><i class="fa-solid fa-envelope"></i
              ></span>
              <input
                type="email"
                id="email"
                v-model="email"
                class="form-control"
                placeholder="Email del usuario"
                required
              />
            </div>
            <div class="input-group mb-3">
              <span class="input-group-text"
                ><i class="fa-solid fa-lock"></i
              ></span>
              <input
                type="password"
                id="password"
                v-model="password"
                class="form-control"
                placeholder="Contraseña"
                required
              />
            </div>
            <div class="d-grid col-6 mx-auto">
              <button class="btn btn-success">
                <i class="fa-solid fa-plus"></i> Crear
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
  
  <script>
import { show_alert, editar } from "../funciones";
import { useRoute } from "vue-router";
import axios from "axios";
export default {
  data() {
    return {
      id: 0,
      name: "",
      email: "",
      password: "",
      url: "http://127.0.0.1:8000/users",
    };
  },
  mounted() {
    const route = useRoute();
    this.id = route.params.id;
    this.url = this.url + "/" + this.id;
    this.getUser();
  },
  methods: {
    getUser() {
      axios
        .get(this.url)
        .then(
          (response) => (
            (this.name = response.data["name"]),
            (this.email = response.data["email"]),
            (this.password = response.data["password"])
          )
        );
    },
    guardar() {
      event.preventDefault();
      if (this.name.trim() === "") {
        show_alert("Ingresa el nombre", "warning", "nombre");
      } else if (this.email.trim() === "") {
        show_alert("Ingresa el email", "warning", "email");
      } else if (this.password.trim() === "") {
        show_alert("Ingresa la contraseña", "warning", "password");
      } else {
        editar(this.id, {
          name: this.name.trim(),
          email: this.email.trim(),
          password: this.password.trim(),
        });
      }
    },
  },
};
</script>