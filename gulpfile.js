var gulp = require("gulp")
var sass = require("gulp-sass")
var sourcemaps = require("gulp-sourcemaps")

var path = {
	sass: {
		source: "./public/sass/**/*.scss",
		destination: "./public/sass",
		map: "."
	}
}

gulp.task('sass', () => {
	return gulp.src(path.sass.source)
	.pipe(sourcemaps.init())
	.pipe(sass().on('error',sass.logError))
	.pipe(sourcemaps.write(path.sass.map))
	.pipe(gulp.dest(path.sass.destination))
})

gulp.task('default', ['sass'] , () => {})

gulp.task('watch', () => {
	gulp.watch(path.sass.source, ['sass'])
})