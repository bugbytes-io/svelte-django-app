<script>
    import {FilmStore} from '../../film-store'

    let handleClick = () => FilmStore.update(prev => {
        let newFilm = {id: 3, name: 'Drive', director: 'Nicolas Winding Refn'}
        return [...prev, newFilm]
    })
</script>

<div>
    <h2 class="my-4">Film List</h2>
    
    <div class="my-4 row">
        {#each $FilmStore as film}
        <div class="col-12 col-sm-6 col-md-4">
            
            <div class="card w-100 h-100">
                <img class="card-img-top" style="height: 300px; object-fit: cover" 
                    src="" 
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