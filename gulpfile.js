const gulp = require('gulp');
const babel = require('gulp-babel');
var uglyfly = require('gulp-uglyfly');

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

gulp.task('default', ['scss']);
