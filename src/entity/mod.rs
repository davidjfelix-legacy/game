#![allow(dead_code)]
mod entity {

    use std::rc::Rc;
    use std::ops::{
        Add,
        Sub,
    };
    
    struct Vec3f64 {
        x: f64,
        y: f64,
        z: f64,
    }

    stuct Vec4f64 {
        x: f64,
        y: f64,
        z: f64,

    struct Entity {
        mass: Rc<Chunk>,
        velocity: Vec3f64,
        location: Vec3f64,
        rotation: Vec3f64,
    }

    impl Entity {
        fn tick(&self, time_delta: f64, acceleration: Vec3f64) {
            mass.tick(time_delta);
        }
    }

    impl Add<Vec3f64> for Vec3f64 {
        fn add(self, _rhs: Vec3f64) -> Vec3f64 {
            Vec3f64 {
                x: self.x + _rhs.x,
                y: self.y + _rhs.y,
                z: self.z + _rhs.z
            }
        }
    }

    impl Sub<Vec3f64> for Vec3f64 {
        fn sub(self, _rhs: Vec3f64) -> Vec3f64 {
            Vec3f64 {
                x: self.x + _rhs.x,
                y: self.y + _rhs.y,
                z: self.z + _rhs.z
        }
    }
}
