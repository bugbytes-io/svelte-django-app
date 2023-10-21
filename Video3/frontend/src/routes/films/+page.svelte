<script>
    import {FilmStore} from '../../film-store'
    import {onMount} from 'svelte'

    onMount(async function () {
        if (!$FilmStore.length) {
            const endpoint = 'http://localhost:8000/api/films/'
            const response = await fetch(endpoint)
            const data = await response.json() 
            FilmStore.set(data)
        }

    })
</script>

<div>
    <h2 class="my-4">Film List</h2>
    
    <div class="my-4 row">
        {#each $FilmStore as film}
        <div class="col-12 col-sm-6 col-md-4">
            
            <div class="card w-100 h-100">
                <img class="card-img-top" style="height: 300px; object-fit: cover" 
                    src="{film.image}" 
                    alt="Film">
                <div class="card-body d-flex flex-column justify-content-between gap-4">
					<div>
                        <h5 class="card-title">{ film.name }</h5>
                        <p class="card-text">Directed by { film.director }</p>
                    </div>
                    <div>
                        <a href="/films/{film.id}" class="btn btn-primary">View</a>
					</div>
                </div>
              </div>

        </div>
        {/each}
    </div>
    
</div>