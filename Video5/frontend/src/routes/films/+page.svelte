<script>
    import {FilmStore} from '../../film-store'
    import {onMount} from 'svelte'

    let tags = []
    let selectedTag = '';

    $: filteredFilms = $FilmStore.filter(film => {
        return selectedTag == '' || film.tags.includes(selectedTag)
    })

    let setTags = () => {
        let tagSet = new Set();
        $FilmStore.map(film => film.tags.forEach(tag => tagSet.add(tag)));
        tags = Array.from(tagSet)
    }

    onMount(async function () {
        if (!$FilmStore.length) {
            const endpoint = 'http://localhost:8000/api/films/'
            const response = await fetch(endpoint)
            const data = await response.json() 
            FilmStore.set(data)
        }
        setTags()
    })

    let handleDelete = (id) => {
        const endpoint = `http://localhost:8000/api/films/${id}`
        fetch(endpoint, {method: 'DELETE'}).then(response => {
            if (response.status == 204) {
                FilmStore.update(prev => prev.filter(film => film.id != id))
                setTags()
            }
        })
    }
</script>

<div>
    <h2 class="my-4">Film List</h2>

    <div class="my-4">
        {#each tags as tag}
            <button class="btn btn-sm btn-warning me-2 mb-1"
                on:click={() => selectedTag = tag}>{tag}</button>
        {/each }
        <button class="btn btn-sm btn-warning me-2 mb-1"
            on:click={() => selectedTag = ''}>ALL</button>
    </div>
    
    <div class="my-4 row">
        {#each filteredFilms as film}
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

                        <button on:click={() => handleDelete(film.id)} class="btn btn-danger ml-2">
                            Delete 
                        </button>
                        <div class="mt-3">
                            {#each film.tags as tag}
                                <div class="d-inline-flex p-2 border me-1 mb-1">{tag}</div>
                            {/each }
                        </div>
					</div>
                </div>
              </div>

        </div>
        {/each}
    </div>
    
</div>