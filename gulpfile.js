const gulp = require('gulp');
const cssScss = require('gulp-css-scss');
const babel = require('gulp-babel');
var uglyfly = require('gulp-uglyfly');

gulp.task('css-scss', () => {
  return gulp.src('static/css/scss/app.scss')
    .pipe(cssScss())
    .pipe(gulp.dest('static/css/app.css'));
});

gulp.task('compress', function() {
  gulp.src('static/css/app.css')
    .pipe(uglyfly())
    .pipe(gulp.dest('static/css/dist'))
});


gulp.task('babel', () => {
    return gulp.src('static/js/dev-app.js')
        .pipe(babel({
            presets: ['es2015']
        }))
        .pipe(gulp.dest('static/js/app.js'));
});

gulp.task('default', ['css-scss']);
