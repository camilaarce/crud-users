<template>
  <div class="row">
    <div class="col-lg-8 offset-lg-2">
      <div class="table-responsive">
        <table class="table table-bordered table-hover">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nombre</th>
              <th>Email</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody class="table-group-divider" id="contenido">
            <tr v-for="(user, i) in users" :key="user.id">
              <td>{{ i }}</td>
              <td>{{ user.name }}</td>
              <td>{{ user.email }}</td>
              <td>
                <router-link
                  :to="{ path: 'edit/' + user.id }"
                  class="btn btn-primary"
                >
                  <i class="fa-solid fa-edit"></i>
                </router-link>
                &nbsp;
                <button
                  class="btn btn-danger"
                  v-on:click="this.delete(user.id, user.name)"
                >
                  <i class="fa-solid fa-trash"></i>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { eliminar } from "../funciones";

export default {
  data() {
    return { users: null };
  },
  mounted() {
    this.getUsers();
  },
  methods: {
    getUsers() {
      axios
        .get("http://127.0.0.1:8000/users")
        .then((response) => (this.users = response.data));
    },
    delete(id, nombre) {
      eliminar(id, nombre);
    },
  },
};
</script>