<script>
    import {FilmStore} from '../../../film-store'
    import { onMount } from "svelte";

    export let data;
    let film;

    onMount(async function() {
        if ($FilmStore.length) {
            film = $FilmStore.find(film => film.id == data.id)
        } else {
            const endpoint = `http://localhost:8000/api/films/${data.id}/`
            let response = await fetch(endpoint)
            if (response.status == 200) {
                film = await response.json()
            } else {
                film = null;
            }
        }
    })

</script>

<div class="row mt-4">
    {#if film }
        <h2 class="mb-4">{ film.name }</h2>
        <div class="col-12 col-md-4">
            <img src="{ film.image }" alt="Film" class="w-100"/>
        </div>
        <div class="col-12 col-md-8">
            <p class="mb-2"><b>{ film.name }</b>, directed by <i>{ film.director }</i></p>
            <p class="mb-2">{ film.description }</p>
        </div>
    {:else }
        <p>No film was found with ID {data.id}</p>
    {/if }
</div>