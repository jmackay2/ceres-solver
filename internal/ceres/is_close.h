// Ceres Solver - A fast non-linear least squares minimizer
// Copyright 2016 Google Inc. All rights reserved.
// http://ceres-solver.org/
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
//
// * Redistributions of source code must retain the above copyright notice,
//   this list of conditions and the following disclaimer.
// * Redistributions in binary form must reproduce the above copyright notice,
//   this list of conditions and the following disclaimer in the documentation
//   and/or other materials provided with the distribution.
// * Neither the name of Google Inc. nor the names of its contributors may be
//   used to endorse or promote products derived from this software without
//   specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
// ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
// LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
// CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
// SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
// INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
// CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
// ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
// POSSIBILITY OF SUCH DAMAGE.
//
// Authors: keir@google.com (Keir Mierle), dgossow@google.com (David Gossow)
//
// Utility routine for comparing two values.

#ifndef CERES_INTERNAL_IS_CLOSE_H_
#define CERES_INTERNAL_IS_CLOSE_H_

#include "ceres/internal/port.h"

namespace ceres {
namespace internal {
// Returns true if x and y have a relative (unsigned) difference less than
// relative_precision and false otherwise. Stores the relative and absolute
// difference in relative/absolute_error if non-nullptr. If one of the two values
// is exactly zero, the absolute difference will be compared, and relative_error
// will be set to the absolute difference.
CERES_EXPORT_INTERNAL bool IsClose(double x,
                                   double y,
                                   double relative_precision,
                                   double* relative_error,
                                   double* absolute_error);
}  // namespace internal
}  // namespace ceres

#endif  // CERES_INTERNAL_IS_CLOSE_H_
